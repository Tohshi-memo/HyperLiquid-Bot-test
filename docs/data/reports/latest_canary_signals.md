# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T11:37:39.440172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0831` n `12`; crypto_alt avg `-0.403` n `228`; crypto_major avg `-0.3364` n `8`; equity avg `-0.17` n `77`; fx avg `-0.001` n `6`; index avg `-0.0275` n `23`; metal avg `-0.0494` n `18`; unknown avg `-0.019` n `687`
- 1h: commodity avg `0.1116` n `12`; crypto_alt avg `-0.5421` n `228`; crypto_major avg `-0.4218` n `8`; equity avg `-0.0904` n `77`; fx avg `0.0014` n `6`; index avg `0.0295` n `23`; metal avg `-0.0986` n `18`; unknown avg `0.1024` n `687`
- 4h: commodity avg `-0.2235` n `12`; crypto_alt avg `0.1852` n `228`; crypto_major avg `0.5768` n `8`; equity avg `0.3634` n `77`; fx avg `0.0582` n `6`; index avg `0.1571` n `23`; metal avg `0.5707` n `18`; unknown avg `0.2962` n `687`
- 24h: commodity avg `0.0494` n `12`; crypto_alt avg `-0.331` n `228`; crypto_major avg `1.5068` n `8`; equity avg `1.661` n `76`; fx avg `-0.0688` n `6`; index avg `0.4815` n `23`; metal avg `-0.198` n `18`; unknown avg `0.383` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
