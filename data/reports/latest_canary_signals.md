# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T23:37:19.825591+00:00`
- Correlation status: `ready`
- Asset price records: `498`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `0.142` n `228`; crypto_major avg `0.0131` n `8`; equity avg `0.0209` n `65`; fx avg `-0.0075` n `4`; index avg `0.0112` n `23`; metal avg `-0.0024` n `18`; unknown avg `0.0194` n `356`
- 1h: commodity avg `-0.0691` n `12`; crypto_alt avg `0.0177` n `228`; crypto_major avg `-0.0358` n `8`; equity avg `0.2799` n `65`; fx avg `0.0154` n `4`; index avg `0.0976` n `23`; metal avg `-0.0447` n `18`; unknown avg `-0.0222` n `356`
- 4h: commodity avg `0.2243` n `12`; crypto_alt avg `0.4577` n `228`; crypto_major avg `-0.0883` n `8`; equity avg `0.0516` n `65`; fx avg `0.017` n `4`; index avg `0.0031` n `23`; metal avg `-0.034` n `18`; unknown avg `0.1526` n `356`
- 24h: commodity avg `-1.6202` n `7`; crypto_alt avg `2.3585` n `223`; crypto_major avg `0.3879` n `7`; equity avg `2.0952` n `47`; fx avg `-0.6149` n `4`; index avg `1.4153` n `6`; metal avg `2.8259` n `7`; unknown avg `3.8661` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1302`, n `494`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `494`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1017`, n `490`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0906`, n `490`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0837`, n `490`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `490`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0744`, n `490`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `494`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `490`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `494`, weak_sample_signal
