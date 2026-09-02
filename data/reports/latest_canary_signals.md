# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T01:22:20.613640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.1459` n `232`; crypto_major avg `0.0864` n `8`; equity avg `0.002` n `132`; fx avg `-0.0028` n `6`; index avg `-0.0041` n `26`; metal avg `0.0173` n `20`; unknown avg `3.6777` n `792`
- 1h: commodity avg `0.1514` n `12`; crypto_alt avg `-0.4165` n `232`; crypto_major avg `-0.3444` n `8`; equity avg `-0.1859` n `132`; fx avg `0.0063` n `6`; index avg `-0.0411` n `26`; metal avg `-0.0924` n `20`; unknown avg `0.5063` n `790`
- 4h: commodity avg `0.2655` n `12`; crypto_alt avg `-0.0756` n `232`; crypto_major avg `0.1055` n `8`; equity avg `-0.0736` n `132`; fx avg `-0.05` n `6`; index avg `0.0066` n `26`; metal avg `-0.1074` n `20`; unknown avg `0.3324` n `790`
- 24h: commodity avg `1.0163` n `12`; crypto_alt avg `-1.0578` n `232`; crypto_major avg `-1.8553` n `8`; equity avg `-2.205` n `130`; fx avg `-0.0403` n `6`; index avg `-0.398` n `26`; metal avg `-1.0469` n `20`; unknown avg `-0.314` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0443`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0312`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.029`, n `668`, weak_sample_signal
