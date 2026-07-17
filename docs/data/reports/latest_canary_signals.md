# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T05:37:25.838780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `12`; crypto_alt avg `-0.3207` n `230`; crypto_major avg `-0.2948` n `8`; equity avg `-0.2835` n `96`; fx avg `-0.0109` n `6`; index avg `-0.0431` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.4821` n `768`
- 1h: commodity avg `-0.0671` n `12`; crypto_alt avg `-0.2453` n `230`; crypto_major avg `-0.4166` n `8`; equity avg `-0.4485` n `96`; fx avg `-0.0124` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0411` n `20`; unknown avg `-0.5949` n `768`
- 4h: commodity avg `-0.1453` n `12`; crypto_alt avg `-0.6656` n `230`; crypto_major avg `-1.1405` n `8`; equity avg `-1.4945` n `94`; fx avg `-0.0128` n `6`; index avg `-0.2509` n `25`; metal avg `-0.2216` n `20`; unknown avg `0.1583` n `768`
- 24h: commodity avg `-0.073` n `12`; crypto_alt avg `-2.3476` n `230`; crypto_major avg `-3.852` n `8`; equity avg `-6.0888` n `94`; fx avg `-0.1322` n `6`; index avg `-0.8256` n `25`; metal avg `-0.8701` n `20`; unknown avg `-0.5638` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
