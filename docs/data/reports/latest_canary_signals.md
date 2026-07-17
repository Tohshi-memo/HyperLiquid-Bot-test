# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T03:37:23.794522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.0352` n `230`; crypto_major avg `-0.0309` n `8`; equity avg `-0.0794` n `94`; fx avg `0.0006` n `6`; index avg `-0.0331` n `25`; metal avg `-0.0311` n `20`; unknown avg `0.0878` n `769`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `0.6991` n `230`; crypto_major avg `0.4007` n `8`; equity avg `0.4087` n `94`; fx avg `0.0129` n `6`; index avg `0.0216` n `25`; metal avg `0.1451` n `20`; unknown avg `0.1713` n `768`
- 4h: commodity avg `-0.0647` n `12`; crypto_alt avg `0.1829` n `230`; crypto_major avg `0.0096` n `8`; equity avg `-1.0068` n `94`; fx avg `-0.0095` n `6`; index avg `-0.1853` n `25`; metal avg `-0.0359` n `20`; unknown avg `-0.0863` n `768`
- 24h: commodity avg `-0.0576` n `12`; crypto_alt avg `-1.6694` n `230`; crypto_major avg `-2.6765` n `8`; equity avg `-5.13` n `94`; fx avg `-0.1246` n `6`; index avg `-0.6536` n `25`; metal avg `-0.7371` n `20`; unknown avg `-0.3046` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
