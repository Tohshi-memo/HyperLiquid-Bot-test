# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T03:07:17.609321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0725` n `12`; crypto_alt avg `0.0085` n `228`; crypto_major avg `0.0234` n `8`; equity avg `-0.077` n `67`; fx avg `-0.0072` n `6`; index avg `-0.0022` n `23`; metal avg `0.0382` n `18`; unknown avg `-0.0768` n `419`
- 1h: commodity avg `0.314` n `12`; crypto_alt avg `-0.1061` n `228`; crypto_major avg `0.0507` n `8`; equity avg `-0.3589` n `67`; fx avg `-0.0065` n `6`; index avg `-0.1634` n `23`; metal avg `-0.0356` n `18`; unknown avg `-0.1357` n `419`
- 4h: commodity avg `0.4728` n `12`; crypto_alt avg `-0.4435` n `228`; crypto_major avg `-0.2536` n `8`; equity avg `-0.712` n `67`; fx avg `-0.0033` n `6`; index avg `-0.2794` n `23`; metal avg `-1.1404` n `18`; unknown avg `0.4573` n `419`
- 24h: commodity avg `-0.0905` n `12`; crypto_alt avg `-2.3897` n `228`; crypto_major avg `-2.1305` n `8`; equity avg `-1.174` n `67`; fx avg `-0.0356` n `6`; index avg `-0.9528` n `23`; metal avg `-2.4274` n `18`; unknown avg `-1.1953` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
