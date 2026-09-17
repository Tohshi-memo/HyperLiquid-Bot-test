# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T22:07:32.042365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.1256` n `234`; crypto_major avg `0.0482` n `8`; equity avg `-0.0504` n `140`; fx avg `0.0251` n `6`; index avg `-0.0189` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.3068` n `893`
- 1h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0322` n `234`; crypto_major avg `0.0015` n `8`; equity avg `-0.0139` n `140`; fx avg `0.0147` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.1281` n `885`
- 4h: commodity avg `-0.1689` n `12`; crypto_alt avg `-0.1231` n `234`; crypto_major avg `0.0399` n `8`; equity avg `0.0557` n `140`; fx avg `0.0015` n `6`; index avg `-0.0331` n `26`; metal avg `-0.1496` n `20`; unknown avg `0.8667` n `833`
- 24h: commodity avg `-0.2161` n `12`; crypto_alt avg `4.1632` n `234`; crypto_major avg `2.389` n `8`; equity avg `2.3073` n `138`; fx avg `0.0059` n `6`; index avg `0.4308` n `26`; metal avg `0.5771` n `20`; unknown avg `1.7756` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
