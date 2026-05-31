# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T14:37:22.214705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0549` n `12`; crypto_alt avg `0.1778` n `228`; crypto_major avg `0.0573` n `8`; equity avg `0.0254` n `69`; fx avg `0.0` n `6`; index avg `0.0588` n `23`; metal avg `0.0194` n `18`; unknown avg `-0.0357` n `421`
- 1h: commodity avg `0.0688` n `12`; crypto_alt avg `-1.0878` n `228`; crypto_major avg `-0.643` n `8`; equity avg `-0.1135` n `69`; fx avg `-0.0045` n `6`; index avg `0.0498` n `23`; metal avg `-0.0018` n `18`; unknown avg `-0.3166` n `421`
- 4h: commodity avg `0.2216` n `12`; crypto_alt avg `-0.5318` n `228`; crypto_major avg `-0.2162` n `8`; equity avg `0.0002` n `69`; fx avg `-0.019` n `6`; index avg `0.0005` n `23`; metal avg `0.0087` n `18`; unknown avg `-0.2203` n `421`
- 24h: commodity avg `0.1532` n `12`; crypto_alt avg `-1.0631` n `228`; crypto_major avg `0.2074` n `8`; equity avg `0.664` n `69`; fx avg `-0.0225` n `6`; index avg `-0.2476` n `23`; metal avg `-0.0501` n `18`; unknown avg `0.0622` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
