# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T22:37:26.886946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.029` n `13`; crypto_alt avg `-0.0114` n `239`; crypto_major avg `-0.0852` n `8`; equity avg `0.1001` n `162`; fx avg `-0.0028` n `6`; index avg `0.0108` n `27`; metal avg `0.0106` n `20`; unknown avg `0.5704` n `1261`
- 1h: commodity avg `0.0112` n `13`; crypto_alt avg `-0.2361` n `239`; crypto_major avg `-0.3708` n `8`; equity avg `-0.1708` n `162`; fx avg `-0.0159` n `6`; index avg `-0.0199` n `27`; metal avg `0.0422` n `20`; unknown avg `11.3629` n `1247`
- 4h: commodity avg `0.2717` n `13`; crypto_alt avg `0.4696` n `239`; crypto_major avg `-0.1598` n `8`; equity avg `-0.3673` n `162`; fx avg `0.0049` n `6`; index avg `-0.0335` n `27`; metal avg `-0.0719` n `20`; unknown avg `0.0473` n `1219`
- 24h: commodity avg `0.8994` n `13`; crypto_alt avg `-1.3642` n `239`; crypto_major avg `-2.3815` n `8`; equity avg `-1.2686` n `162`; fx avg `-0.1333` n `6`; index avg `-0.0109` n `27`; metal avg `-0.7068` n `20`; unknown avg `50.9843` n `1153`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
