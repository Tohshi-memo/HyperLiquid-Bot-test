# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T09:37:18.256393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2819` n `12`; crypto_alt avg `-0.3185` n `228`; crypto_major avg `-0.2475` n `8`; equity avg `0.0304` n `66`; fx avg `0.0104` n `6`; index avg `0.0183` n `23`; metal avg `-0.0632` n `18`; unknown avg `0.8202` n `386`
- 1h: commodity avg `-0.6831` n `12`; crypto_alt avg `-0.284` n `228`; crypto_major avg `-0.1736` n `8`; equity avg `0.1591` n `66`; fx avg `-0.0007` n `6`; index avg `0.0665` n `23`; metal avg `0.215` n `18`; unknown avg `0.8355` n `386`
- 4h: commodity avg `-0.7053` n `12`; crypto_alt avg `0.2623` n `228`; crypto_major avg `0.4554` n `8`; equity avg `0.0728` n `66`; fx avg `-0.0162` n `6`; index avg `0.0456` n `23`; metal avg `0.4087` n `18`; unknown avg `1.2158` n `374`
- 24h: commodity avg `-2.3461` n `12`; crypto_alt avg `2.3203` n `228`; crypto_major avg `3.1491` n `8`; equity avg `1.8875` n `66`; fx avg `0.1035` n `6`; index avg `1.36` n `23`; metal avg `0.4991` n `18`; unknown avg `8.0896` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
