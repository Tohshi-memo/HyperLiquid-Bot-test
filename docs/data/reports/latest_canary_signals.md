# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T13:07:29.165061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.0677` n `228`; crypto_major avg `0.1354` n `8`; equity avg `0.1671` n `74`; fx avg `-0.002` n `6`; index avg `0.0198` n `23`; metal avg `-0.0028` n `18`; unknown avg `0.1442` n `645`
- 1h: commodity avg `0.1774` n `12`; crypto_alt avg `-0.2486` n `228`; crypto_major avg `-0.1852` n `8`; equity avg `-0.0582` n `74`; fx avg `0.0019` n `6`; index avg `0.0474` n `23`; metal avg `-0.0595` n `18`; unknown avg `0.0715` n `645`
- 4h: commodity avg `0.2892` n `12`; crypto_alt avg `-0.4063` n `228`; crypto_major avg `-0.0753` n `8`; equity avg `0.184` n `74`; fx avg `0.0277` n `6`; index avg `0.1583` n `23`; metal avg `-0.1036` n `18`; unknown avg `0.362` n `629`
- 24h: commodity avg `-0.2111` n `12`; crypto_alt avg `-0.6518` n `228`; crypto_major avg `-0.0791` n `8`; equity avg `0.7652` n `74`; fx avg `0.0073` n `6`; index avg `0.1835` n `23`; metal avg `0.0752` n `18`; unknown avg `-1.0567` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
