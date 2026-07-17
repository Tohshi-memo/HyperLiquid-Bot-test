# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T03:07:24.117311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `0.4622` n `230`; crypto_major avg `0.3696` n `8`; equity avg `0.368` n `94`; fx avg `0.0023` n `6`; index avg `0.0155` n `25`; metal avg `0.1169` n `20`; unknown avg `0.0559` n `768`
- 1h: commodity avg `-0.0478` n `12`; crypto_alt avg `0.1508` n `230`; crypto_major avg `0.1092` n `8`; equity avg `-0.2947` n `94`; fx avg `0.0208` n `6`; index avg `-0.0278` n `25`; metal avg `0.009` n `20`; unknown avg `-0.2169` n `768`
- 4h: commodity avg `-0.0389` n `12`; crypto_alt avg `-0.3523` n `230`; crypto_major avg `-0.3935` n `8`; equity avg `-1.4466` n `94`; fx avg `0.0017` n `6`; index avg `-0.2367` n `25`; metal avg `-0.0849` n `20`; unknown avg `-0.4548` n `768`
- 24h: commodity avg `-0.1307` n `12`; crypto_alt avg `-2.0795` n `230`; crypto_major avg `-2.8594` n `8`; equity avg `-5.3014` n `94`; fx avg `-0.1365` n `6`; index avg `-0.7076` n `25`; metal avg `-0.7569` n `20`; unknown avg `-0.6937` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
