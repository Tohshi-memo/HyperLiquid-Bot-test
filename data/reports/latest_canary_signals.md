# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T12:46:06.399047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0716` n `12`; crypto_alt avg `-0.0938` n `228`; crypto_major avg `-0.1117` n `8`; equity avg `-0.0447` n `86`; fx avg `-0.0018` n `6`; index avg `-0.0047` n `23`; metal avg `0.0085` n `20`; unknown avg `-0.0501` n `764`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.0957` n `228`; crypto_major avg `-0.2144` n `8`; equity avg `-0.4987` n `86`; fx avg `-0.0395` n `6`; index avg `-0.0992` n `23`; metal avg `-0.0362` n `20`; unknown avg `0.0197` n `764`
- 4h: commodity avg `-0.0964` n `12`; crypto_alt avg `0.4494` n `228`; crypto_major avg `0.1159` n `8`; equity avg `0.2172` n `86`; fx avg `-0.0655` n `6`; index avg `-0.0496` n `23`; metal avg `0.0303` n `20`; unknown avg `-0.2754` n `764`
- 24h: commodity avg `-0.4161` n `12`; crypto_alt avg `-4.7331` n `228`; crypto_major avg `-5.0352` n `8`; equity avg `-4.699` n `85`; fx avg `-0.199` n `6`; index avg `-0.9922` n `23`; metal avg `-1.3207` n `20`; unknown avg `0.078` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
