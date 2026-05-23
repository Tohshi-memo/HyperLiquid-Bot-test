# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T15:37:15.070925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.0937` n `228`; crypto_major avg `-0.2105` n `8`; equity avg `-0.0392` n `67`; fx avg `0.0155` n `6`; index avg `-0.0063` n `23`; metal avg `-0.0113` n `18`; unknown avg `0.2159` n `396`
- 1h: commodity avg `0.2909` n `12`; crypto_alt avg `0.6482` n `228`; crypto_major avg `0.5496` n `8`; equity avg `0.2873` n `67`; fx avg `0.0101` n `6`; index avg `-0.054` n `23`; metal avg `0.0947` n `18`; unknown avg `0.6564` n `396`
- 4h: commodity avg `-0.5353` n `12`; crypto_alt avg `1.9875` n `228`; crypto_major avg `1.3905` n `8`; equity avg `0.7232` n `67`; fx avg `0.0003` n `6`; index avg `0.4336` n `23`; metal avg `0.2154` n `18`; unknown avg `1.1789` n `396`
- 24h: commodity avg `0.0991` n `12`; crypto_alt avg `-3.2676` n `228`; crypto_major avg `-2.2641` n `8`; equity avg `-0.9344` n `67`; fx avg `0.0691` n `6`; index avg `-0.1286` n `23`; metal avg `-0.152` n `18`; unknown avg `-2.2955` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
