# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T07:00:17.369972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.42` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `0.0227` n `234`; crypto_major avg `-0.0053` n `8`; equity avg `0.0148` n `140`; fx avg `0.0011` n `6`; index avg `-0.0004` n `26`; metal avg `0.0002` n `20`; unknown avg `0.2245` n `941`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.2824` n `234`; crypto_major avg `0.0105` n `8`; equity avg `-0.0055` n `140`; fx avg `-0.017` n `6`; index avg `-0.0045` n `26`; metal avg `0.0056` n `20`; unknown avg `0.1822` n `941`
- 4h: commodity avg `0.0145` n `12`; crypto_alt avg `-0.1916` n `234`; crypto_major avg `-0.0817` n `8`; equity avg `-0.0463` n `140`; fx avg `-0.0108` n `6`; index avg `-0.0149` n `26`; metal avg `0.0189` n `20`; unknown avg `1.0392` n `895`
- 24h: commodity avg `0.2644` n `12`; crypto_alt avg `-0.2085` n `234`; crypto_major avg `-1.8247` n `8`; equity avg `-0.202` n `140`; fx avg `-0.0793` n `6`; index avg `-0.0394` n `26`; metal avg `0.0084` n `20`; unknown avg `0.831` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
