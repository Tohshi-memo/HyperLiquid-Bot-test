# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T03:52:28.623218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.1891` n `231`; crypto_major avg `-0.2251` n `8`; equity avg `-0.105` n `126`; fx avg `-0.0026` n `6`; index avg `-0.0181` n `25`; metal avg `-0.0503` n `20`; unknown avg `-0.1734` n `793`
- 1h: commodity avg `0.075` n `12`; crypto_alt avg `0.0858` n `231`; crypto_major avg `-0.1051` n `8`; equity avg `-0.066` n `126`; fx avg `-0.0043` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0283` n `20`; unknown avg `0.1615` n `793`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `-0.9532` n `231`; crypto_major avg `-0.9075` n `8`; equity avg `-0.3681` n `126`; fx avg `-0.0434` n `6`; index avg `-0.1285` n `25`; metal avg `0.0341` n `20`; unknown avg `0.1784` n `793`
- 24h: commodity avg `0.4981` n `12`; crypto_alt avg `0.2595` n `231`; crypto_major avg `0.3791` n `8`; equity avg `1.1006` n `126`; fx avg `-0.1121` n `6`; index avg `0.1392` n `25`; metal avg `-0.2354` n `20`; unknown avg `0.3346` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
