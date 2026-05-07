# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T22:46:34.999918+00:00`
- Correlation status: `ready`
- Asset price records: `591`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.0713` n `228`; crypto_major avg `0.0094` n `8`; equity avg `0.1062` n `65`; fx avg `-0.0056` n `5`; index avg `-0.0222` n `23`; metal avg `-0.1033` n `18`; unknown avg `0.0082` n `365`
- 1h: commodity avg `-0.1512` n `12`; crypto_alt avg `-0.1787` n `228`; crypto_major avg `-0.281` n `8`; equity avg `0.1615` n `65`; fx avg `0.0092` n `5`; index avg `0.0892` n `23`; metal avg `-0.0619` n `18`; unknown avg `-0.0957` n `365`
- 4h: commodity avg `0.4976` n `12`; crypto_alt avg `-0.1121` n `228`; crypto_major avg `-0.321` n `8`; equity avg `-0.3302` n `65`; fx avg `-0.0417` n `5`; index avg `0.0546` n `23`; metal avg `-0.3714` n `18`; unknown avg `-0.7282` n `365`
- 24h: commodity avg `0.843` n `12`; crypto_alt avg `1.1035` n `228`; crypto_major avg `-1.999` n `8`; equity avg `-1.6282` n `65`; fx avg `0.1598` n `5`; index avg `-0.8926` n `23`; metal avg `-0.4664` n `18`; unknown avg `-0.4917` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `587`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `587`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `587`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `587`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `583`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `583`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `583`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0875`, n `583`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `583`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `583`, weak_sample_signal
