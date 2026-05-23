# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T03:37:17.687008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1388` n `12`; crypto_alt avg `0.0819` n `228`; crypto_major avg `0.0272` n `8`; equity avg `-0.0126` n `67`; fx avg `0.0` n `6`; index avg `0.0034` n `23`; metal avg `-0.0363` n `18`; unknown avg `0.0344` n `386`
- 1h: commodity avg `0.1556` n `12`; crypto_alt avg `0.5428` n `228`; crypto_major avg `0.3226` n `8`; equity avg `0.0527` n `67`; fx avg `0.0003` n `6`; index avg `0.0572` n `23`; metal avg `0.029` n `18`; unknown avg `-0.1037` n `386`
- 4h: commodity avg `0.1286` n `12`; crypto_alt avg `0.3839` n `228`; crypto_major avg `-0.0958` n `8`; equity avg `-0.2238` n `67`; fx avg `-0.0078` n `6`; index avg `-0.005` n `23`; metal avg `-0.0775` n `18`; unknown avg `-0.9852` n `386`
- 24h: commodity avg `0.1292` n `12`; crypto_alt avg `-3.1871` n `228`; crypto_major avg `-2.4081` n `8`; equity avg `-1.7291` n `67`; fx avg `0.0667` n `6`; index avg `0.0563` n `23`; metal avg `-0.7543` n `18`; unknown avg `-2.0084` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
