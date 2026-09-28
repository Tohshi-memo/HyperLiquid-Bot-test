# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T22:31:26.181852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2175` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0768` n `234`; crypto_major avg `0.0348` n `8`; equity avg `-0.0061` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0341` n `20`; unknown avg `0.0212` n `963`
- 1h: commodity avg `-0.1077` n `12`; crypto_alt avg `-0.5942` n `234`; crypto_major avg `-0.4363` n `8`; equity avg `-0.0076` n `141`; fx avg `0.0075` n `6`; index avg `0.0033` n `26`; metal avg `0.0285` n `20`; unknown avg `-0.1719` n `937`
- 4h: commodity avg `0.2343` n `12`; crypto_alt avg `-1.4443` n `234`; crypto_major avg `-1.2424` n `8`; equity avg `-0.2562` n `141`; fx avg `0.0017` n `6`; index avg `-0.0249` n `26`; metal avg `-0.1431` n `20`; unknown avg `0.3711` n `833`
- 24h: commodity avg `0.0178` n `12`; crypto_alt avg `-3.8647` n `234`; crypto_major avg `-1.9031` n `8`; equity avg `-2.9597` n `141`; fx avg `0.0534` n `6`; index avg `-0.1995` n `26`; metal avg `-0.9567` n `20`; unknown avg `53.2963` n `800`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
