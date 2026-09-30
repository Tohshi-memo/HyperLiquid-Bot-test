# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T04:52:25.383683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `-0.0578` n `234`; crypto_major avg `-0.1584` n `8`; equity avg `-0.0571` n `142`; fx avg `0.0086` n `6`; index avg `-0.0195` n `26`; metal avg `-0.0221` n `20`; unknown avg `2.1927` n `963`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.5662` n `234`; crypto_major avg `0.0553` n `8`; equity avg `0.1173` n `142`; fx avg `0.0328` n `6`; index avg `0.0218` n `26`; metal avg `0.0234` n `20`; unknown avg `1.0944` n `955`
- 4h: commodity avg `0.0587` n `12`; crypto_alt avg `0.5862` n `234`; crypto_major avg `0.0852` n `8`; equity avg `-0.0057` n `142`; fx avg `-0.0577` n `6`; index avg `0.0171` n `26`; metal avg `-0.0873` n `20`; unknown avg `2.695` n `955`
- 24h: commodity avg `-0.9735` n `12`; crypto_alt avg `1.7452` n `234`; crypto_major avg `0.1828` n `8`; equity avg `1.1799` n `142`; fx avg `-0.1154` n `6`; index avg `0.2049` n `26`; metal avg `0.2445` n `20`; unknown avg `3238.1045` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
