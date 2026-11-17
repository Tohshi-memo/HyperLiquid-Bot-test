# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T12:22:25.426179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `13`; crypto_alt avg `0.0848` n `239`; crypto_major avg `0.0108` n `8`; equity avg `0.1743` n `162`; fx avg `0.0032` n `6`; index avg `0.0202` n `27`; metal avg `-0.0026` n `20`; unknown avg `0.1552` n `1264`
- 1h: commodity avg `0.0567` n `13`; crypto_alt avg `0.5628` n `239`; crypto_major avg `0.5356` n `8`; equity avg `1.098` n `162`; fx avg `0.0167` n `6`; index avg `0.0776` n `27`; metal avg `0.0779` n `20`; unknown avg `0.7616` n `1256`
- 4h: commodity avg `0.2113` n `13`; crypto_alt avg `0.4964` n `239`; crypto_major avg `0.234` n `8`; equity avg `0.9174` n `162`; fx avg `-0.0236` n `6`; index avg `0.0628` n `27`; metal avg `0.0719` n `20`; unknown avg `22.9546` n `1254`
- 24h: commodity avg `-0.5692` n `13`; crypto_alt avg `1.9465` n `239`; crypto_major avg `1.9497` n `8`; equity avg `-0.5616` n `162`; fx avg `-0.0415` n `6`; index avg `-0.0546` n `27`; metal avg `-0.0988` n `20`; unknown avg `9.4934` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
