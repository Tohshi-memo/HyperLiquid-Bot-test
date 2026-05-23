# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T12:52:18.004892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.1292` n `228`; crypto_major avg `0.0457` n `8`; equity avg `0.0648` n `67`; fx avg `0.0` n `6`; index avg `0.084` n `23`; metal avg `0.0029` n `18`; unknown avg `0.034` n `396`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `0.103` n `228`; crypto_major avg `-0.0041` n `8`; equity avg `0.0541` n `67`; fx avg `0.0001` n `6`; index avg `0.1094` n `23`; metal avg `-0.0013` n `18`; unknown avg `0.0475` n `396`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `0.1361` n `228`; crypto_major avg `0.0013` n `8`; equity avg `0.1333` n `67`; fx avg `0.0066` n `6`; index avg `0.1521` n `23`; metal avg `-0.0685` n `18`; unknown avg `0.0225` n `396`
- 24h: commodity avg `0.496` n `12`; crypto_alt avg `-6.382` n `228`; crypto_major avg `-4.7161` n `8`; equity avg `-1.887` n `67`; fx avg `0.0575` n `6`; index avg `-0.1191` n `23`; metal avg `-0.4453` n `18`; unknown avg `-2.0877` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0649`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0575`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0554`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0554`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0538`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0519`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0463`, n `669`, weak_sample_signal
