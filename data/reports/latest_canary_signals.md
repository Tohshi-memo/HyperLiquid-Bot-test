# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T04:52:37.944386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0594` n `230`; crypto_major avg `-0.0549` n `8`; equity avg `0.1338` n `100`; fx avg `0.0039` n `6`; index avg `0.0483` n `25`; metal avg `-0.0117` n `20`; unknown avg `-0.0825` n `775`
- 1h: commodity avg `-0.1239` n `12`; crypto_alt avg `0.0133` n `230`; crypto_major avg `0.1215` n `8`; equity avg `0.2579` n `100`; fx avg `0.0109` n `6`; index avg `0.0872` n `25`; metal avg `-0.0025` n `20`; unknown avg `0.0384` n `775`
- 4h: commodity avg `-0.0605` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `0.1576` n `8`; equity avg `0.1506` n `100`; fx avg `0.0274` n `6`; index avg `-0.0356` n `25`; metal avg `-0.137` n `20`; unknown avg `-0.4611` n `775`
- 24h: commodity avg `-0.5387` n `12`; crypto_alt avg `1.0882` n `230`; crypto_major avg `1.2359` n `8`; equity avg `0.9` n `100`; fx avg `0.0757` n `6`; index avg `0.1144` n `25`; metal avg `0.3086` n `20`; unknown avg `-0.0294` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
