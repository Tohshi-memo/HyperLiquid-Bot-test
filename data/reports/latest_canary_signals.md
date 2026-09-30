# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T12:37:33.276810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.0894` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7931` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `0.9535` n `234`; crypto_major avg `0.8879` n `8`; equity avg `0.5846` n `142`; fx avg `0.001` n `6`; index avg `0.1373` n `26`; metal avg `0.1989` n `20`; unknown avg `8.7994` n `963`
- 1h: commodity avg `-0.0885` n `12`; crypto_alt avg `0.903` n `234`; crypto_major avg `0.8628` n `8`; equity avg `0.4781` n `142`; fx avg `-0.0113` n `6`; index avg `0.1106` n `26`; metal avg `0.1144` n `20`; unknown avg `8.4446` n `955`
- 4h: commodity avg `0.167` n `12`; crypto_alt avg `1.7988` n `234`; crypto_major avg `2.0406` n `8`; equity avg `0.2475` n `142`; fx avg `0.0724` n `6`; index avg `0.0376` n `26`; metal avg `-0.0488` n `20`; unknown avg `5.695` n `955`
- 24h: commodity avg `-0.1592` n `12`; crypto_alt avg `0.3202` n `234`; crypto_major avg `-0.2234` n `8`; equity avg `0.2545` n `142`; fx avg `0.0526` n `6`; index avg `0.0902` n `26`; metal avg `0.2308` n `20`; unknown avg `2684.7999` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
