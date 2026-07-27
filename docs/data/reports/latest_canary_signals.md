# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T02:37:26.546008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `0.053` n `230`; crypto_major avg `0.0277` n `8`; equity avg `0.0655` n `100`; fx avg `-0.0164` n `6`; index avg `0.017` n `25`; metal avg `-0.0563` n `20`; unknown avg `-0.1573` n `775`
- 1h: commodity avg `0.0545` n `12`; crypto_alt avg `0.3226` n `230`; crypto_major avg `0.3162` n `8`; equity avg `0.5463` n `100`; fx avg `0.0202` n `6`; index avg `0.0581` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.3115` n `775`
- 4h: commodity avg `0.1746` n `12`; crypto_alt avg `-0.0262` n `230`; crypto_major avg `-0.259` n `8`; equity avg `-0.1912` n `100`; fx avg `0.1002` n `6`; index avg `-0.1063` n `25`; metal avg `-0.017` n `20`; unknown avg `-0.5765` n `775`
- 24h: commodity avg `-0.4883` n `12`; crypto_alt avg `1.5626` n `230`; crypto_major avg `1.3778` n `8`; equity avg `0.727` n `100`; fx avg `0.15` n `6`; index avg `0.0706` n `25`; metal avg `0.3948` n `20`; unknown avg `-0.0062` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
