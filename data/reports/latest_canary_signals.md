# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T08:52:23.784128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.0125` n `230`; crypto_major avg `-0.0845` n `8`; equity avg `-0.0888` n `102`; fx avg `-0.0767` n `6`; index avg `0.0135` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.0164` n `782`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.1108` n `230`; crypto_major avg `-0.2643` n `8`; equity avg `0.0605` n `102`; fx avg `-0.0683` n `6`; index avg `0.0204` n `25`; metal avg `-0.0142` n `20`; unknown avg `-0.0582` n `782`
- 4h: commodity avg `-0.068` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `-0.3594` n `8`; equity avg `0.0981` n `102`; fx avg `-0.1301` n `6`; index avg `0.0635` n `25`; metal avg `0.006` n `20`; unknown avg `0.2801` n `766`
- 24h: commodity avg `-1.1801` n `12`; crypto_alt avg `0.2569` n `230`; crypto_major avg `0.1694` n `8`; equity avg `0.9157` n `102`; fx avg `-0.2356` n `6`; index avg `0.2792` n `25`; metal avg `0.2353` n `20`; unknown avg `0.2553` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
