# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T18:22:31.086628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.1959` n `239`; crypto_major avg `-0.0786` n `8`; equity avg `-0.0569` n `162`; fx avg `0.016` n `6`; index avg `-0.0059` n `27`; metal avg `0.003` n `20`; unknown avg `-0.086` n `1263`
- 1h: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.1798` n `239`; crypto_major avg `-0.1359` n `8`; equity avg `-0.1448` n `162`; fx avg `0.0177` n `6`; index avg `0.0014` n `27`; metal avg `0.0376` n `20`; unknown avg `2.5228` n `1261`
- 4h: commodity avg `0.0221` n `13`; crypto_alt avg `-0.9103` n `239`; crypto_major avg `-0.882` n `8`; equity avg `-0.0313` n `162`; fx avg `0.0259` n `6`; index avg `0.0068` n `27`; metal avg `0.0219` n `20`; unknown avg `360.4949` n `1256`
- 24h: commodity avg `0.0447` n `13`; crypto_alt avg `-1.0742` n `239`; crypto_major avg `-0.5099` n `8`; equity avg `0.1844` n `162`; fx avg `0.0015` n `6`; index avg `0.0452` n `27`; metal avg `-0.0994` n `20`; unknown avg `2.6914` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
