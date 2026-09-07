# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T00:37:26.893775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0459` n `232`; crypto_major avg `-0.0273` n `8`; equity avg `-0.0156` n `134`; fx avg `-0.0636` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0193` n `20`; unknown avg `3.1875` n `788`
- 1h: commodity avg `-0.0483` n `12`; crypto_alt avg `0.1746` n `232`; crypto_major avg `-0.1921` n `8`; equity avg `0.1757` n `134`; fx avg `-0.1222` n `6`; index avg `0.0215` n `26`; metal avg `-0.0243` n `20`; unknown avg `1.881` n `782`
- 4h: commodity avg `-0.014` n `12`; crypto_alt avg `0.7448` n `232`; crypto_major avg `0.3549` n `8`; equity avg `0.0994` n `134`; fx avg `-0.0837` n `6`; index avg `-0.0095` n `26`; metal avg `-0.1003` n `20`; unknown avg `146.6515` n `777`
- 24h: commodity avg `-0.0442` n `12`; crypto_alt avg `1.4281` n `232`; crypto_major avg `0.726` n `8`; equity avg `0.3597` n `134`; fx avg `-0.0724` n `6`; index avg `0.0099` n `26`; metal avg `-0.1091` n `20`; unknown avg `151.0348` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
