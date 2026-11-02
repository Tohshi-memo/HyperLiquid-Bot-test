# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T08:22:30.181322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `-0.1882` n `238`; crypto_major avg `-0.0955` n `8`; equity avg `-0.0946` n `156`; fx avg `0.0164` n `6`; index avg `-0.0356` n `27`; metal avg `-0.0303` n `20`; unknown avg `0.9606` n `1264`
- 1h: commodity avg `-0.0652` n `13`; crypto_alt avg `-0.1435` n `238`; crypto_major avg `0.0667` n `8`; equity avg `-0.1003` n `156`; fx avg `0.0085` n `6`; index avg `-0.0254` n `27`; metal avg `-0.0791` n `20`; unknown avg `4.4508` n `1172`
- 4h: commodity avg `-0.0307` n `13`; crypto_alt avg `-1.4229` n `238`; crypto_major avg `-1.0611` n `8`; equity avg `-0.5143` n `156`; fx avg `0.0271` n `6`; index avg `-0.0842` n `27`; metal avg `0.0104` n `20`; unknown avg `0.4966` n `1153`
- 24h: commodity avg `-0.491` n `13`; crypto_alt avg `-1.8748` n `238`; crypto_major avg `-0.2106` n `8`; equity avg `0.9146` n `156`; fx avg `0.2464` n `6`; index avg `0.2725` n `27`; metal avg `0.0918` n `20`; unknown avg `2.3017` n `1067`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
