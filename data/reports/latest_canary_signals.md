# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T16:52:45.839386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.0594` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.0587` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0228` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.029` n `13`; crypto_alt avg `-0.0805` n `239`; crypto_major avg `-0.1363` n `8`; equity avg `-0.289` n `164`; fx avg `0.0102` n `6`; index avg `-0.0225` n `27`; metal avg `0.012` n `20`; unknown avg `0.74` n `1265`
- 1h: commodity avg `-0.1021` n `13`; crypto_alt avg `-0.5564` n `239`; crypto_major avg `-0.8606` n `8`; equity avg `-0.5438` n `164`; fx avg `-0.013` n `6`; index avg `-0.0265` n `27`; metal avg `-0.072` n `20`; unknown avg `4.6288` n `1257`
- 4h: commodity avg `-0.1412` n `13`; crypto_alt avg `-1.4859` n `239`; crypto_major avg `-2.1999` n `8`; equity avg `-2.1162` n `164`; fx avg `-0.0219` n `6`; index avg `-0.1771` n `27`; metal avg `-0.1405` n `20`; unknown avg `2.6393` n `1257`
- 24h: commodity avg `-0.3549` n `13`; crypto_alt avg `-0.1303` n `239`; crypto_major avg `-0.6938` n `8`; equity avg `0.2763` n `164`; fx avg `-0.1953` n `6`; index avg `0.067` n `27`; metal avg `-1.1947` n `20`; unknown avg `0.1534` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
