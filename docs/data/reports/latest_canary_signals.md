# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T14:22:29.481832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.31` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.7976` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.7044` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0983` n `12`; crypto_alt avg `-0.8669` n `234`; crypto_major avg `-0.7155` n `8`; equity avg `-0.0545` n `142`; fx avg `-0.0183` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0368` n `20`; unknown avg `10.5916` n `941`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `-1.603` n `234`; crypto_major avg `-1.7306` n `8`; equity avg `-0.2667` n `142`; fx avg `-0.0225` n `6`; index avg `0.067` n `26`; metal avg `-0.0262` n `20`; unknown avg `22.1738` n `907`
- 4h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.0329` n `234`; crypto_major avg `-0.1835` n `8`; equity avg `0.2935` n `142`; fx avg `-0.0451` n `6`; index avg `0.1534` n `26`; metal avg `-0.0799` n `20`; unknown avg `14.1028` n `901`
- 24h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.7708` n `234`; crypto_major avg `-1.0103` n `8`; equity avg `-0.3632` n `142`; fx avg `0.015` n `6`; index avg `0.1367` n `26`; metal avg `0.0201` n `20`; unknown avg `9200.5454` n `836`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
