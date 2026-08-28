# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T03:07:24.475418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3919` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0324` n `12`; crypto_alt avg `-0.0664` n `231`; crypto_major avg `-0.1122` n `8`; equity avg `0.0494` n `127`; fx avg `-0.0113` n `6`; index avg `0.0094` n `26`; metal avg `0.0104` n `20`; unknown avg `0.0835` n `792`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `-1.5641` n `231`; crypto_major avg `-0.9156` n `8`; equity avg `-0.1826` n `127`; fx avg `0.0011` n `6`; index avg `-0.005` n `26`; metal avg `0.0627` n `20`; unknown avg `0.3906` n `792`
- 4h: commodity avg `-0.0415` n `12`; crypto_alt avg `-1.6289` n `231`; crypto_major avg `-1.3227` n `8`; equity avg `0.0913` n `127`; fx avg `-0.0481` n `6`; index avg `0.0692` n `26`; metal avg `-0.1155` n `20`; unknown avg `0.3589` n `792`
- 24h: commodity avg `0.3087` n `12`; crypto_alt avg `0.1041` n `231`; crypto_major avg `1.3671` n `8`; equity avg `-0.059` n `127`; fx avg `-0.0344` n `6`; index avg `0.0393` n `26`; metal avg `-0.1343` n `20`; unknown avg `0.5017` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
