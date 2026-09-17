# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T20:22:28.980767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `0.1885` n `234`; crypto_major avg `0.1307` n `8`; equity avg `-0.0033` n `140`; fx avg `-0.0014` n `6`; index avg `-0.011` n `26`; metal avg `-0.0098` n `20`; unknown avg `3.6859` n `919`
- 1h: commodity avg `-0.0116` n `12`; crypto_alt avg `0.3795` n `234`; crypto_major avg `0.4765` n `8`; equity avg `0.0545` n `140`; fx avg `-0.0018` n `6`; index avg `-0.0202` n `26`; metal avg `-0.025` n `20`; unknown avg `18.4945` n `891`
- 4h: commodity avg `-0.0359` n `12`; crypto_alt avg `0.4157` n `234`; crypto_major avg `0.1896` n `8`; equity avg `0.0498` n `140`; fx avg `0.0172` n `6`; index avg `-0.0184` n `26`; metal avg `-0.2067` n `20`; unknown avg `3.7503` n `885`
- 24h: commodity avg `-0.1744` n `12`; crypto_alt avg `4.1028` n `234`; crypto_major avg `1.6197` n `8`; equity avg `2.4499` n `138`; fx avg `-0.0281` n `6`; index avg `0.4525` n `26`; metal avg `0.5843` n `20`; unknown avg `5.7373` n `771`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
