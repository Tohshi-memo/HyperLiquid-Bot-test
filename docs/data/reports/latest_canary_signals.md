# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T00:07:30.044922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `12`; crypto_alt avg `-0.0397` n `234`; crypto_major avg `-0.0345` n `8`; equity avg `-0.0283` n `142`; fx avg `0.0241` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0518` n `20`; unknown avg `0.3392` n `957`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `-0.0726` n `234`; crypto_major avg `-0.1598` n `8`; equity avg `0.0407` n `142`; fx avg `0.0319` n `6`; index avg `0.0073` n `26`; metal avg `-0.0346` n `20`; unknown avg `0.6496` n `957`
- 4h: commodity avg `-0.1008` n `12`; crypto_alt avg `0.609` n `234`; crypto_major avg `0.4619` n `8`; equity avg `0.2731` n `142`; fx avg `0.0467` n `6`; index avg `0.0777` n `26`; metal avg `-0.0191` n `20`; unknown avg `0.1424` n `891`
- 24h: commodity avg `0.1616` n `12`; crypto_alt avg `0.88` n `234`; crypto_major avg `0.8288` n `8`; equity avg `-0.4531` n `142`; fx avg `0.123` n `6`; index avg `-0.0494` n `26`; metal avg `-0.3191` n `20`; unknown avg `769.985` n `803`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
