# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T21:37:40.539578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `13`; crypto_alt avg `0.4009` n `239`; crypto_major avg `0.3405` n `8`; equity avg `0.8504` n `163`; fx avg `0.0002` n `6`; index avg `0.0625` n `27`; metal avg `0.0643` n `20`; unknown avg `2.9423` n `1265`
- 1h: commodity avg `-0.0258` n `13`; crypto_alt avg `0.4745` n `239`; crypto_major avg `0.5352` n `8`; equity avg `1.6089` n `163`; fx avg `-0.0173` n `6`; index avg `0.1509` n `27`; metal avg `0.0767` n `20`; unknown avg `4.28` n `1247`
- 4h: commodity avg `-0.0541` n `13`; crypto_alt avg `1.2564` n `239`; crypto_major avg `1.3411` n `8`; equity avg `1.6721` n `163`; fx avg `-0.0348` n `6`; index avg `0.1494` n `27`; metal avg `-0.0583` n `20`; unknown avg `1.8223` n `1239`
- 24h: commodity avg `0.2438` n `13`; crypto_alt avg `0.4968` n `239`; crypto_major avg `0.4021` n `8`; equity avg `0.1784` n `163`; fx avg `0.0243` n `6`; index avg `-0.0027` n `27`; metal avg `0.0171` n `20`; unknown avg `6.3335` n `1107`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
