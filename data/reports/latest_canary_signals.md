# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T06:52:32.353599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6673` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `0.1945` n `234`; crypto_major avg `0.1724` n `8`; equity avg `0.0364` n `141`; fx avg `0.0164` n `6`; index avg `0.0091` n `26`; metal avg `-0.0248` n `20`; unknown avg `-0.0946` n `963`
- 1h: commodity avg `-0.0349` n `12`; crypto_alt avg `0.8466` n `234`; crypto_major avg `0.7652` n `8`; equity avg `0.6279` n `141`; fx avg `0.0228` n `6`; index avg `0.1291` n `26`; metal avg `0.0585` n `20`; unknown avg `1.3578` n `943`
- 4h: commodity avg `-0.0384` n `12`; crypto_alt avg `2.4799` n `234`; crypto_major avg `1.6876` n `8`; equity avg `0.4911` n `141`; fx avg `-0.0317` n `6`; index avg `0.0892` n `26`; metal avg `0.0203` n `20`; unknown avg `2.2768` n `937`
- 24h: commodity avg `0.1387` n `12`; crypto_alt avg `-0.2909` n `234`; crypto_major avg `0.7203` n `8`; equity avg `-0.918` n `140`; fx avg `-0.0798` n `6`; index avg `-0.0464` n `23`; metal avg `-0.3852` n `18`; unknown avg `69.6368` n `790`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
