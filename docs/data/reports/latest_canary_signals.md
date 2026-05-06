# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T16:22:15.524703+00:00`
- Correlation status: `ready`
- Asset price records: `469`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `7.25` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.2037` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.616` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.523` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1885` n `12`; crypto_alt avg `-0.2217` n `228`; crypto_major avg `-0.22` n `8`; equity avg `-0.053` n `65`; fx avg `-0.0213` n `4`; index avg `-0.0075` n `23`; metal avg `0.0908` n `18`; unknown avg `-0.0723` n `356`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `0.0579` n `228`; crypto_major avg `-0.198` n `8`; equity avg `0.0639` n `65`; fx avg `0.008` n `4`; index avg `-0.0553` n `23`; metal avg `-0.1751` n `18`; unknown avg `0.0954` n `356`
- 4h: commodity avg `-0.1053` n `7`; crypto_alt avg `-0.8339` n `223`; crypto_major avg `-1.7436` n `7`; equity avg `-0.2206` n `47`; fx avg `0.0243` n `4`; index avg `-0.1276` n `6`; metal avg `0.4601` n `7`; unknown avg `8.8846` n `313`
- 24h: commodity avg `-2.4772` n `7`; crypto_alt avg `2.8946` n `223`; crypto_major avg `0.8312` n `7`; equity avg `2.2751` n `47`; fx avg `-0.4414` n `4`; index avg `1.8045` n `6`; metal avg `2.9997` n `7`; unknown avg `17.9291` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2272`, n `465`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1643`, n `461`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1479`, n `461`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1366`, n `465`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1355`, n `465`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1285`, n `461`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `465`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `465`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.114`, n `461`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `465`, weak_sample_signal
