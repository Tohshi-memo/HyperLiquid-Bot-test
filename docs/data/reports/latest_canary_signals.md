# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T03:37:09.805941+00:00`
- Correlation status: `ready`
- Asset price records: `610`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `0.1301` n `228`; crypto_major avg `0.0685` n `8`; equity avg `0.0721` n `65`; fx avg `0.0073` n `5`; index avg `0.0414` n `23`; metal avg `0.2258` n `18`; unknown avg `-0.0626` n `365`
- 1h: commodity avg `-0.3471` n `12`; crypto_alt avg `0.3549` n `228`; crypto_major avg `0.1264` n `8`; equity avg `0.0859` n `65`; fx avg `-0.0214` n `5`; index avg `0.0798` n `23`; metal avg `0.4233` n `18`; unknown avg `-0.2777` n `365`
- 4h: commodity avg `-0.6263` n `12`; crypto_alt avg `0.0148` n `228`; crypto_major avg `-0.2421` n `8`; equity avg `0.4266` n `65`; fx avg `0.122` n `5`; index avg `0.3457` n `23`; metal avg `0.8515` n `18`; unknown avg `-0.2916` n `365`
- 24h: commodity avg `0.38` n `12`; crypto_alt avg `2.4522` n `228`; crypto_major avg `-1.0644` n `8`; equity avg `-0.9795` n `65`; fx avg `0.1664` n `5`; index avg `-0.5955` n `23`; metal avg `0.5336` n `18`; unknown avg `0.1034` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.131`, n `606`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `606`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `606`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `606`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1079`, n `602`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1059`, n `602`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `602`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `602`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0791`, n `602`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `606`, weak_sample_signal
