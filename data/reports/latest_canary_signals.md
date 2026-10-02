# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T22:52:29.335770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `13`; crypto_alt avg `0.0569` n `235`; crypto_major avg `0.0408` n `8`; equity avg `-0.0106` n `143`; fx avg `0.0027` n `6`; index avg `0.0127` n `26`; metal avg `0.015` n `20`; unknown avg `-0.0931` n `984`
- 1h: commodity avg `0.0564` n `13`; crypto_alt avg `0.4099` n `235`; crypto_major avg `0.3753` n `8`; equity avg `0.0207` n `143`; fx avg `-0.0014` n `6`; index avg `-0.0119` n `26`; metal avg `0.021` n `20`; unknown avg `0.5097` n `974`
- 4h: commodity avg `0.3571` n `13`; crypto_alt avg `0.7371` n `235`; crypto_major avg `0.5511` n `8`; equity avg `0.1274` n `143`; fx avg `-0.0206` n `6`; index avg `0.0382` n `26`; metal avg `0.0773` n `20`; unknown avg `0.162` n `906`
- 24h: commodity avg `0.13` n `13`; crypto_alt avg `-0.6209` n `235`; crypto_major avg `-0.3901` n `8`; equity avg `0.7361` n `142`; fx avg `-0.1565` n `6`; index avg `0.2978` n `26`; metal avg `-0.2145` n `20`; unknown avg `-0.4274` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
