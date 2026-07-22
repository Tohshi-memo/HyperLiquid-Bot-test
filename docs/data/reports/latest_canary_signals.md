# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T01:11:38.946849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1199` n `12`; crypto_alt avg `-0.1063` n `230`; crypto_major avg `-0.1296` n `8`; equity avg `-0.1309` n `98`; fx avg `0.0014` n `6`; index avg `0.0005` n `25`; metal avg `0.2505` n `20`; unknown avg `-0.0906` n `771`
- 1h: commodity avg `0.1178` n `12`; crypto_alt avg `0.0072` n `230`; crypto_major avg `0.0068` n `8`; equity avg `-0.3698` n `98`; fx avg `0.001` n `6`; index avg `-0.0662` n `25`; metal avg `0.2697` n `20`; unknown avg `-0.0876` n `771`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `0.1211` n `230`; crypto_major avg `0.2957` n `8`; equity avg `-0.0094` n `98`; fx avg `0.0043` n `6`; index avg `0.0152` n `25`; metal avg `0.346` n `20`; unknown avg `-0.1427` n `771`
- 24h: commodity avg `0.6672` n `12`; crypto_alt avg `0.5915` n `230`; crypto_major avg `0.5481` n `8`; equity avg `3.7864` n `98`; fx avg `0.0136` n `6`; index avg `0.5487` n `25`; metal avg `0.9409` n `20`; unknown avg `0.3746` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0962`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0579`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.051`, n `666`, weak_sample_signal
