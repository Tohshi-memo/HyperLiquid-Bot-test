# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T20:07:31.801607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0879` n `234`; crypto_major avg `0.1018` n `8`; equity avg `0.0546` n `140`; fx avg `-0.0056` n `6`; index avg `-0.0199` n `26`; metal avg `-0.0162` n `20`; unknown avg `5.6954` n `891`
- 1h: commodity avg `-0.0844` n `12`; crypto_alt avg `0.1334` n `234`; crypto_major avg `0.3899` n `8`; equity avg `0.0309` n `140`; fx avg `-0.0006` n `6`; index avg `-0.0172` n `26`; metal avg `-0.0611` n `20`; unknown avg `10.3366` n `891`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.279` n `234`; crypto_major avg `0.1174` n `8`; equity avg `0.1621` n `140`; fx avg `0.0296` n `6`; index avg `0.0043` n `26`; metal avg `-0.2026` n `20`; unknown avg `3.2936` n `885`
- 24h: commodity avg `-0.1915` n `12`; crypto_alt avg `4.0783` n `234`; crypto_major avg `1.604` n `8`; equity avg `2.5071` n `138`; fx avg `-0.0171` n `6`; index avg `0.4656` n `26`; metal avg `0.567` n `20`; unknown avg `4.0786` n `763`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
