# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T10:37:18.532130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.7508` n `12`; crypto_alt avg `-0.4871` n `228`; crypto_major avg `-0.2902` n `8`; equity avg `-0.2892` n `66`; fx avg `0.0114` n `6`; index avg `-0.204` n `23`; metal avg `-0.4488` n `18`; unknown avg `1.2835` n `386`
- 1h: commodity avg `0.9761` n `12`; crypto_alt avg `-0.5172` n `228`; crypto_major avg `-0.4861` n `8`; equity avg `-0.4433` n `66`; fx avg `0.0103` n `6`; index avg `-0.2682` n `23`; metal avg `-0.483` n `18`; unknown avg `1.3182` n `386`
- 4h: commodity avg `0.1562` n `12`; crypto_alt avg `-0.2096` n `228`; crypto_major avg `0.107` n `8`; equity avg `-0.1654` n `66`; fx avg `-0.0007` n `6`; index avg `-0.1129` n `23`; metal avg `-0.058` n `18`; unknown avg `1.2471` n `385`
- 24h: commodity avg `-1.0089` n `12`; crypto_alt avg `1.728` n `228`; crypto_major avg `2.3989` n `8`; equity avg `1.2159` n `66`; fx avg `0.1119` n `6`; index avg `1.0577` n `23`; metal avg `-0.1987` n `18`; unknown avg `7.2848` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
