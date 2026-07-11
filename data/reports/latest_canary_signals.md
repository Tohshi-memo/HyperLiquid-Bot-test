# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T06:22:26.081837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.2006` n `230`; crypto_major avg `0.1557` n `8`; equity avg `0.0139` n `92`; fx avg `-0.0006` n `6`; index avg `0.0018` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0178` n `765`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `0.152` n `230`; crypto_major avg `0.1009` n `8`; equity avg `0.0278` n `92`; fx avg `0.0125` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0205` n `733`
- 4h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.1133` n `229`; crypto_major avg `0.2529` n `8`; equity avg `0.0289` n `92`; fx avg `0.0349` n `6`; index avg `0.0076` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.0672` n `731`
- 24h: commodity avg `-0.3025` n `12`; crypto_alt avg `0.5279` n `229`; crypto_major avg `-0.0607` n `8`; equity avg `-0.094` n `92`; fx avg `-0.0332` n `6`; index avg `0.1594` n `25`; metal avg `-0.028` n `20`; unknown avg `4.1688` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
