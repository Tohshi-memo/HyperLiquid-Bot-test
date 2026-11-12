# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T01:37:29.315311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1867` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0526` n `13`; crypto_alt avg `0.2079` n `239`; crypto_major avg `0.0999` n `8`; equity avg `0.3749` n `161`; fx avg `-0.0075` n `6`; index avg `0.0381` n `27`; metal avg `0.0053` n `20`; unknown avg `0.0876` n `1262`
- 1h: commodity avg `-0.1116` n `13`; crypto_alt avg `-0.4472` n `239`; crypto_major avg `-0.4307` n `8`; equity avg `0.0783` n `161`; fx avg `0.0128` n `6`; index avg `-0.0082` n `27`; metal avg `0.0818` n `20`; unknown avg `20.177` n `1256`
- 4h: commodity avg `-0.1357` n `13`; crypto_alt avg `-1.2093` n `239`; crypto_major avg `-1.3056` n `8`; equity avg `-1.3094` n `161`; fx avg `-0.039` n `6`; index avg `-0.1189` n `27`; metal avg `0.0428` n `20`; unknown avg `3.9691` n `1242`
- 24h: commodity avg `0.1476` n `13`; crypto_alt avg `-1.852` n `239`; crypto_major avg `-0.7555` n `8`; equity avg `1.2854` n `161`; fx avg `-0.1454` n `6`; index avg `0.1081` n `27`; metal avg `-0.3055` n `20`; unknown avg `4.4556` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
