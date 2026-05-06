# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T15:07:25.938669+00:00`
- Correlation status: `ready`
- Asset price records: `464`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `10.17` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-3.0484` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2227` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1099` n `12`; crypto_alt avg `0.1676` n `228`; crypto_major avg `-0.0284` n `8`; equity avg `-0.0129` n `65`; fx avg `0.0004` n `4`; index avg `0.0189` n `23`; metal avg `0.0025` n `18`; unknown avg `0.0602` n `356`
- 1h: commodity avg `-0.549` n `12`; crypto_alt avg `0.9312` n `228`; crypto_major avg `0.4555` n `8`; equity avg `0.7552` n `65`; fx avg `-0.0245` n `4`; index avg `0.3365` n `23`; metal avg `0.2665` n `18`; unknown avg `2.3821` n `356`
- 4h: commodity avg `1.4455` n `7`; crypto_alt avg `-1.2291` n `223`; crypto_major avg `-1.6029` n `7`; equity avg `-0.949` n `47`; fx avg `0.1145` n `4`; index avg `-0.3802` n `6`; metal avg `-0.1485` n `7`; unknown avg `8.0569` n `313`
- 24h: commodity avg `-2.683` n `7`; crypto_alt avg `2.4923` n `223`; crypto_major avg `0.9142` n `7`; equity avg `2.0826` n `47`; fx avg `-0.6176` n `4`; index avg `2.0979` n `6`; metal avg `2.6845` n `7`; unknown avg `19.4792` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.3371`, n `460`, moderate_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.2985`, n `460`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1558`, n `460`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1558`, n `456`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1467`, n `456`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `460`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `460`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1213`, n `456`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `460`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `460`, weak_sample_signal
