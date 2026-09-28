# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T21:22:33.161250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0054` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.2443` n `234`; crypto_major avg `-0.2205` n `8`; equity avg `0.0433` n `141`; fx avg `-0.0014` n `6`; index avg `0.009` n `26`; metal avg `0.0152` n `20`; unknown avg `12.1553` n `963`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `-0.1898` n `234`; crypto_major avg `-0.2307` n `8`; equity avg `0.0977` n `141`; fx avg `0.0044` n `6`; index avg `0.0209` n `26`; metal avg `-0.0383` n `20`; unknown avg `13.0533` n `959`
- 4h: commodity avg `0.265` n `12`; crypto_alt avg `-0.7594` n `234`; crypto_major avg `-1.0359` n `8`; equity avg `-0.3174` n `141`; fx avg `0.0123` n `6`; index avg `-0.0305` n `26`; metal avg `-0.2035` n `20`; unknown avg `-0.0045` n `857`
- 24h: commodity avg `-0.3128` n `12`; crypto_alt avg `-3.9218` n `234`; crypto_major avg `-2.2661` n `8`; equity avg `-3.3062` n `141`; fx avg `0.0958` n `6`; index avg `-0.3037` n `26`; metal avg `-1.1361` n `20`; unknown avg `27.2635` n `796`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
