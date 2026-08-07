# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T15:52:27.470108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `12`; crypto_alt avg `-0.0196` n `230`; crypto_major avg `-0.0188` n `8`; equity avg `-0.0134` n `112`; fx avg `-0.004` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0586` n `20`; unknown avg `-0.0484` n `782`
- 1h: commodity avg `0.104` n `12`; crypto_alt avg `0.2997` n `230`; crypto_major avg `0.0683` n `8`; equity avg `0.8774` n `112`; fx avg `-0.0146` n `6`; index avg `0.0969` n `25`; metal avg `-0.0581` n `20`; unknown avg `0.0031` n `782`
- 4h: commodity avg `0.4611` n `12`; crypto_alt avg `-0.1736` n `230`; crypto_major avg `-0.0953` n `8`; equity avg `0.5297` n `112`; fx avg `-0.0432` n `6`; index avg `0.0497` n `25`; metal avg `-0.1087` n `20`; unknown avg `-0.0084` n `782`
- 24h: commodity avg `0.3938` n `12`; crypto_alt avg `-0.2608` n `230`; crypto_major avg `-0.0209` n `8`; equity avg `0.9203` n `112`; fx avg `-0.1318` n `6`; index avg `0.0088` n `25`; metal avg `0.2544` n `20`; unknown avg `0.0494` n `765`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
