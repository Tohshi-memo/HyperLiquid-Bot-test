# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T13:52:33.559739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0134` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0749` n `12`; crypto_alt avg `0.2317` n `234`; crypto_major avg `-0.0039` n `8`; equity avg `-0.1197` n `142`; fx avg `-0.0052` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0673` n `20`; unknown avg `0.8386` n `963`
- 1h: commodity avg `0.0326` n `12`; crypto_alt avg `-0.7537` n `234`; crypto_major avg `-1.0526` n `8`; equity avg `-0.4782` n `142`; fx avg `0.0008` n `6`; index avg `-0.0392` n `26`; metal avg `-0.1937` n `20`; unknown avg `119.3715` n `961`
- 4h: commodity avg `0.0405` n `12`; crypto_alt avg `0.5905` n `234`; crypto_major avg `0.7781` n `8`; equity avg `0.0085` n `142`; fx avg `-0.0148` n `6`; index avg `0.0544` n `26`; metal avg `-0.0857` n `20`; unknown avg `4.7494` n `955`
- 24h: commodity avg `0.0554` n `12`; crypto_alt avg `-0.0866` n `234`; crypto_major avg `-0.564` n `8`; equity avg `-0.1455` n `142`; fx avg `0.0048` n `6`; index avg `0.0837` n `26`; metal avg `0.053` n `20`; unknown avg `2925.085` n `826`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
