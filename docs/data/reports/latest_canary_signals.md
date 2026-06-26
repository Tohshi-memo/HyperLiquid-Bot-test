# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T13:07:26.912522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8322` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5555` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0657` n `12`; crypto_alt avg `-0.122` n `228`; crypto_major avg `-0.2805` n `8`; equity avg `-0.2211` n `86`; fx avg `0.0214` n `6`; index avg `-0.0285` n `23`; metal avg `-0.0084` n `20`; unknown avg `-0.0662` n `765`
- 1h: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.4707` n `228`; crypto_major avg `-0.565` n `8`; equity avg `-0.5964` n `86`; fx avg `0.036` n `6`; index avg `-0.0871` n `23`; metal avg `-0.0022` n `20`; unknown avg `-0.1172` n `765`
- 4h: commodity avg `0.0526` n `12`; crypto_alt avg `-1.3739` n `228`; crypto_major avg `-1.65` n `8`; equity avg `-0.621` n `86`; fx avg `0.035` n `6`; index avg `-0.0945` n `23`; metal avg `0.1822` n `20`; unknown avg `-0.2327` n `765`
- 24h: commodity avg `-0.0689` n `12`; crypto_alt avg `-2.4982` n `228`; crypto_major avg `-2.8848` n `8`; equity avg `-4.6959` n `86`; fx avg `0.0696` n `6`; index avg `-0.7247` n `23`; metal avg `0.0493` n `20`; unknown avg `0.5797` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3198`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
