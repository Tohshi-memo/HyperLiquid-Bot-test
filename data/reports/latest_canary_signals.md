# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T02:52:29.355910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.0386` n `230`; crypto_major avg `-0.0559` n `8`; equity avg `-0.0558` n `102`; fx avg `0.0107` n `6`; index avg `-0.0057` n `25`; metal avg `0.0461` n `20`; unknown avg `0.0479` n `784`
- 1h: commodity avg `0.0406` n `12`; crypto_alt avg `-0.0637` n `230`; crypto_major avg `-0.0547` n `8`; equity avg `0.1807` n `102`; fx avg `-0.0254` n `6`; index avg `0.0319` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0115` n `784`
- 4h: commodity avg `-0.1452` n `12`; crypto_alt avg `-0.5975` n `230`; crypto_major avg `-0.6835` n `8`; equity avg `0.4191` n `102`; fx avg `-0.272` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0723` n `20`; unknown avg `-0.1245` n `783`
- 24h: commodity avg `-0.3747` n `12`; crypto_alt avg `-0.5707` n `230`; crypto_major avg `-0.1801` n `8`; equity avg `0.9047` n `102`; fx avg `-0.2998` n `6`; index avg `0.0673` n `25`; metal avg `0.0027` n `20`; unknown avg `1.2852` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
