# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T15:52:19.493141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1745` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0773` n `12`; crypto_alt avg `-0.0542` n `228`; crypto_major avg `-0.109` n `8`; equity avg `0.0245` n `67`; fx avg `0.02` n `6`; index avg `0.0046` n `23`; metal avg `-0.0055` n `18`; unknown avg `-0.439` n `386`
- 1h: commodity avg `-0.4067` n `12`; crypto_alt avg `0.0695` n `228`; crypto_major avg `-0.1571` n `8`; equity avg `0.0783` n `67`; fx avg `0.0279` n `6`; index avg `0.15` n `23`; metal avg `0.3249` n `18`; unknown avg `-0.2617` n `386`
- 4h: commodity avg `-0.8018` n `12`; crypto_alt avg `-0.9332` n `228`; crypto_major avg `-0.7381` n `8`; equity avg `-0.0051` n `67`; fx avg `0.0164` n `6`; index avg `0.4364` n `23`; metal avg `-0.5007` n `18`; unknown avg `0.5426` n `386`
- 24h: commodity avg `-2.326` n `12`; crypto_alt avg `0.7978` n `228`; crypto_major avg `-0.5702` n `8`; equity avg `0.902` n `67`; fx avg `0.168` n `6`; index avg `1.2913` n `23`; metal avg `-0.0269` n `18`; unknown avg `-0.4849` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0435`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0399`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0353`, n `668`, weak_sample_signal
