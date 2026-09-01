# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T03:22:26.242814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.0594` n `232`; crypto_major avg `0.0315` n `8`; equity avg `-0.0166` n `130`; fx avg `0.0076` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0343` n `20`; unknown avg `-0.0306` n `792`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.2812` n `232`; crypto_major avg `0.1309` n `8`; equity avg `-0.0914` n `130`; fx avg `0.0154` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0855` n `20`; unknown avg `-0.1642` n `790`
- 4h: commodity avg `0.0394` n `12`; crypto_alt avg `0.5624` n `232`; crypto_major avg `-0.0482` n `8`; equity avg `0.0071` n `130`; fx avg `0.02` n `6`; index avg `0.0443` n `26`; metal avg `0.0009` n `20`; unknown avg `0.2822` n `790`
- 24h: commodity avg `0.4159` n `12`; crypto_alt avg `1.7376` n `231`; crypto_major avg `1.5942` n `8`; equity avg `1.1342` n `130`; fx avg `-0.0254` n `6`; index avg `0.1094` n `26`; metal avg `-0.0976` n `20`; unknown avg `0.1983` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
