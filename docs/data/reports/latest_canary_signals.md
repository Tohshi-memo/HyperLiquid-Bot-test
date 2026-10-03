# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T07:37:29.253384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0074` n `13`; crypto_alt avg `-0.1094` n `235`; crypto_major avg `0.0153` n `8`; equity avg `-0.0131` n `143`; fx avg `0.0043` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.0892` n `984`
- 1h: commodity avg `0.0427` n `13`; crypto_alt avg `-0.3981` n `235`; crypto_major avg `-0.1037` n `8`; equity avg `0.0188` n `143`; fx avg `0.013` n `6`; index avg `-0.0013` n `26`; metal avg `0.0029` n `20`; unknown avg `0.2447` n `982`
- 4h: commodity avg `-0.038` n `13`; crypto_alt avg `-0.5237` n `235`; crypto_major avg `-0.1184` n `8`; equity avg `-0.0423` n `143`; fx avg `0.0002` n `6`; index avg `-0.0131` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.0294` n `954`
- 24h: commodity avg `0.2507` n `13`; crypto_alt avg `-1.6915` n `235`; crypto_major avg `-1.6737` n `8`; equity avg `0.423` n `142`; fx avg `0.0078` n `6`; index avg `0.2048` n `26`; metal avg `-0.3094` n `20`; unknown avg `-0.7599` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
