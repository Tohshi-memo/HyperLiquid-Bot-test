# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T22:22:25.202180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.412` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.2149` n `234`; crypto_major avg `0.1698` n `8`; equity avg `0.0574` n `141`; fx avg `-0.0032` n `6`; index avg `0.0109` n `26`; metal avg `0.0074` n `20`; unknown avg `0.2887` n `963`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.6201` n `234`; crypto_major avg `-0.5044` n `8`; equity avg `-0.0165` n `141`; fx avg `-0.0012` n `6`; index avg `0.0057` n `26`; metal avg `0.0475` n `20`; unknown avg `0.2019` n `937`
- 4h: commodity avg `0.2466` n `12`; crypto_alt avg `-1.7025` n `234`; crypto_major avg `-1.4433` n `8`; equity avg `-0.3221` n `141`; fx avg `0.0044` n `6`; index avg `-0.0313` n `26`; metal avg `-0.1362` n `20`; unknown avg `0.6459` n `833`
- 24h: commodity avg `0.0556` n `12`; crypto_alt avg `-3.9902` n `234`; crypto_major avg `-2.297` n `8`; equity avg `-3.0478` n `141`; fx avg `0.0572` n `6`; index avg `-0.2036` n `26`; metal avg `-0.9631` n `20`; unknown avg `31.9052` n `780`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
