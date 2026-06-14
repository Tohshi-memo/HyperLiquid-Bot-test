# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T13:12:07.640236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `-0.0245` n `228`; crypto_major avg `0.0082` n `8`; equity avg `0.0445` n `74`; fx avg `-0.0069` n `6`; index avg `0.0298` n `23`; metal avg `-0.0104` n `18`; unknown avg `0.1891` n `645`
- 1h: commodity avg `0.1785` n `12`; crypto_alt avg `-0.3403` n `228`; crypto_major avg `-0.3119` n `8`; equity avg `-0.1804` n `74`; fx avg `-0.0031` n `6`; index avg `0.0574` n `23`; metal avg `-0.0671` n `18`; unknown avg `0.1171` n `645`
- 4h: commodity avg `0.2903` n `12`; crypto_alt avg `-0.4976` n `228`; crypto_major avg `-0.203` n `8`; equity avg `0.0609` n `74`; fx avg `0.0227` n `6`; index avg `0.1683` n `23`; metal avg `-0.1112` n `18`; unknown avg `0.3735` n `629`
- 24h: commodity avg `-0.21` n `12`; crypto_alt avg `-0.7436` n `228`; crypto_major avg `-0.2074` n `8`; equity avg `0.6415` n `74`; fx avg `0.0023` n `6`; index avg `0.1936` n `23`; metal avg `0.0676` n `18`; unknown avg `-1.2102` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
