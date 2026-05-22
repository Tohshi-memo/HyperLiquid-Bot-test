# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T07:22:21.939473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.5222` n `228`; crypto_major avg `0.2627` n `8`; equity avg `0.0451` n `67`; fx avg `0.0067` n `6`; index avg `0.0204` n `23`; metal avg `0.0666` n `18`; unknown avg `0.0568` n `386`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `0.1016` n `228`; crypto_major avg `-0.1125` n `8`; equity avg `-0.0107` n `67`; fx avg `-0.0322` n `6`; index avg `-0.0203` n `23`; metal avg `-0.1156` n `18`; unknown avg `-0.1303` n `386`
- 4h: commodity avg `0.2832` n `12`; crypto_alt avg `0.1252` n `228`; crypto_major avg `-0.2932` n `8`; equity avg `0.166` n `67`; fx avg `0.0128` n `6`; index avg `0.156` n `23`; metal avg `0.1043` n `18`; unknown avg `-0.3759` n `376`
- 24h: commodity avg `-0.8255` n `12`; crypto_alt avg `1.968` n `228`; crypto_major avg `0.2012` n `8`; equity avg `1.8988` n `66`; fx avg `0.1428` n `6`; index avg `0.9113` n `23`; metal avg `0.838` n `18`; unknown avg `2.4066` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0397`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0391`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
