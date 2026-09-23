# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T10:07:27.946056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0048` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0975` n `12`; crypto_alt avg `0.0615` n `234`; crypto_major avg `0.0682` n `8`; equity avg `0.0209` n `140`; fx avg `0.0079` n `6`; index avg `0.0071` n `26`; metal avg `0.0345` n `20`; unknown avg `0.016` n `943`
- 1h: commodity avg `-0.046` n `12`; crypto_alt avg `0.0736` n `234`; crypto_major avg `-0.2209` n `8`; equity avg `-0.0009` n `140`; fx avg `-0.036` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0288` n `20`; unknown avg `0.1455` n `943`
- 4h: commodity avg `0.1583` n `12`; crypto_alt avg `-0.2514` n `234`; crypto_major avg `-1.0408` n `8`; equity avg `-0.1207` n `140`; fx avg `0.0781` n `6`; index avg `-0.036` n `26`; metal avg `-0.2095` n `20`; unknown avg `-0.1188` n `937`
- 24h: commodity avg `0.6447` n `12`; crypto_alt avg `3.7313` n `234`; crypto_major avg `0.6315` n `8`; equity avg `0.7026` n `140`; fx avg `0.03` n `6`; index avg `0.0316` n `26`; metal avg `-0.0958` n `20`; unknown avg `1.0064` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
